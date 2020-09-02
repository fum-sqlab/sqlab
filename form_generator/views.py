'''
    Created By Sara-Bolouri
    Created At 07-25-2020
'''
from form_generator.models import *
from form_generator.serializers import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .helper import *
from .exception import exceptions
from .status import *

user =[ 
    {
        "id" : 1,
        "username" : "Sara"
    }
]

class FieldView(viewsets.ViewSet):
    def list(self, request):
        fields = Field.objects.all()
        fields_serializer = FieldSerializer(fields, many=True)
        return Response(fields_serializer.data, status=SUCCEEDED_REQUEST)

class FormView(viewsets.ViewSet):

    def list(self, request):
        '''
            Get all Forms
        '''
        forms = Form.objects.all()
        forms_serializer = FormSerializer(forms, many=True)
        return Response(forms_serializer.data, status=SUCCEEDED_REQUEST)

    def create(self, request):
        '''
            Create new Form Object
        '''
        form_data = request.data
        all_fields = form_data.pop('fields')
        form = FormSerializer(data=form_data)
        if form.is_valid():
            form.save()

            for field in all_fields:
                field['field'] = field.pop('field_id')
                field['form'] = form.data.get('id')

                typeof = field.pop('type')
                if typeof == "checkbox" or typeof == "radio":
                    items = field.pop("items")

                new_record = FormFieldSerializer(data=field)
                if new_record.is_valid():
                    new_record.save()

                    if typeof == "checkbox" or typeof == "radio":
                        field_id = new_record.data.get('id')
                        for item in items:
                            item['field'] = field_id
                            choice = ChoiceSerializer(data=item)

                            if choice.is_valid():
                                choice.save()
                            else:
                                return Response(choice.errors, status=INVALID_DATA)

                else:
                    return Response(new_record.errors, status=INVALID_DATA)
        else:
            return Response(form.errors, status=INVALID_DATA)

        return Response("ok", status=CREATED)
    
    def partial_update(self, request, pk=None):
        form = get_object(type_object="form", primary_key=pk)
        fields = request.data["fields"]
        updated_form = FormSerializer(form, data=request.data, partial=True)
        if updated_form.is_valid():
            updated_form.save()
        else:
            return Response(updated_form.errors)
        i = 0
        for field in fields:
            field = get_object(type_object="formfield", primary_key=field["id"])
            updated_field = FormFieldSerializer(field, data=request.data["fields"][i], partial=True)
            if updated_field.is_valid():
                updated_field.save()
            else: return Response(updated_field.errors, status=INVALID_DATA)
            i += 1
        return Response(status=SUCCEEDED_REQUEST)

    def destroy(self, request, pk=None):
        '''
            Delete form object that its 'id' is 'pk'
        '''
        form = get_object(type_object="form", primary_key=pk)
        ffo = filter_for_deleting(type_object="formfield", form=pk)
        pfo = filter_for_deleting(type_object="pageform", form=pk)
        if has_choice(ffo):
            ffo_seri = FormFieldSerializer(ffo, many=True)
            for choice in ffo_seri.data:
                filter_object(type_object="choice", field=choice["id"]).delete()
        if ffo is not None:
            ffo.delete()
        if pfo is not None:
            pfo.delete()
        form.delete()

        return Response(status=DELETED)

    @action(detail=True, methods=['PUT'])
    def add_field_to_form(self, request, field_pk, form_pk):
        details = request.data
        details['field'] = field_pk
        details['form'] = form_pk
        form_field_seri = FormFieldSerializer(data=details)
        if form_field_seri.is_valid():
            form_field_seri.save()
            return Response(form_field_seri.data, status=SUCCEEDED_REQUEST)
        return Response(form_field_seri.errors, status=INVALID_DATA)

    @action(detail=True, methods=['DELETE'])
    def remove_field_from_form(self, request, ff_id):
        result = filter_for_deleting(type_object="formfield", id=ff_id)
        if result is not None:
            result.delete()
        return Response(status=DELETED)

    @action(detail=True, methods=['GET'])
    def show_form_details(self, request, pk=None):
        form_seri = FormSerializer(get_object(type_object="form", primary_key=pk)).data
        ffs = filter_for_deleting(type_object="formfield", form=pk)
        if ffs is not None:
            form_field_seri = FormFieldSerializer(ffs, many=True)
            
            for field in form_field_seri.data:
                field_id = field.pop('field')
                field_seri = FieldSerializer(get_object(type_object="field", primary_key=field_id))
                field_type = field_seri.data.get('field_type')
                field["field_type"] = field_type

                if field_type == "checkbox" or field_type == "radio":
                    field["items"] = get_items(field["id"])

            form_seri['fields'] = form_field_seri.data
        return Response(form_seri, status=SUCCEEDED_REQUEST)
        
class GroupView(viewsets.ViewSet):

    def list(self, request):
        '''
            Get all groups
        '''
        groups = Group.objects.all()
        groups_serializer = GroupSerializer(groups, many=True)
        return Response(groups_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        '''
            Create a new group
        '''
        group_serializer = GroupSerializer(data=request.data)
        if group_serializer.is_valid():
            group_serializer.save()
            return Response(group_serializer.data, status=CREATED)
        return Response(group_serializer.errors, status=INVALID_DATA)

    def destroy(self, request, pk):
        '''
            Delete a group
        '''
        result = filter_for_deleting(type_object="groupform", group=pk)
        if result is not None:
            result.delete()
        get_object(type_object="group", primary_key=pk).delete()
        return Response(status=DELETED)

    def retrive(self, request, pk):
        gp = get_object(type_object="group", primary_key=pk)
        gp_serializer = GroupSerializer(gp)
        return Response(gp_serializer.data, status=SUCCEEDED_REQUEST)

    @action(detail=True, methods=['PUT'])
    def add_form_to_group(self, request, gp_pk, form_pk):
        '''
            Set a form to a specific group
        '''
        form = get_object(type_object="form", primary_key=form_pk)
        group = get_object(type_object="group", primary_key=gp_pk)
        
        group.form.add(*[form])
        group.save()
        return Response("ok", status=SUCCEEDED_REQUEST)  
         
    @action(detail=True, methods=['DELETE'])
    def remove_form_from_group(self, request, gp_pk, form_pk):
        '''
            Remove a from from list of specific group
        '''
        result = filter_for_deleting(type_object="groupform", form=form_pk, group=gp_pk)
        if result is not None:
            result.delete()
            return Response(status=DELETED)
        return Response("No data", status=NOT_FOUND)

class PageView(viewsets.ViewSet):

    def list(self, request):
        '''
            Show all pages
        '''
        pages = Page.objects.all()
        pages_serializer = PageSerializer(pages, many=True)
        return Response(pages_serializer.data, status=SUCCEEDED_REQUEST)

    def create(self, request):
        '''
            Create new page
        '''
        page_data = request.data
        forms = page_data.pop('forms')
        page = PageSerializer(data=page_data)
        if page.is_valid():
            page.save()
        else:
            return Response(page.errors, status=INVALID_DATA)

        for form in forms:
            section_data = {
                "title" : form["section_name"],
                "slug"  : form["slug"],
                "placeholder" : form["placeholder"]
            }
            section = SectionSerializer(data=section_data)
            if section.is_valid():
                section.save()
            else:
                return Response(status=400)
            
            pageForm_details = {
                "page" : page.data["id"],
                "form" : form["id"],
                "section" : section.data["id"]
            }

            pageform = PageFormSerializer(data=pageForm_details)
            if pageform.is_valid():
                pageform.save()
            else:
                return Response(pageform.errors, status=INVALID_DATA)

        return Response("Done",status=SUCCEEDED_REQUEST)
        
    def destroy(self, request, pk=None):
        page = Page.objects.get(pk=pk)
        result = filter_for_deleting(type_object="pageform", page=pk)
        if result is not None:
            result.delete()
        page.delete()
        return Response(status=SUCCEEDED_REQUEST)

    @action(detail=True, methods=['PUT'])
    def add_form_to_page(self, request, page_pk, form_pk):
        get_object(type_object="form", primary_key=form_pk)
        get_object(type_object="page", primary_key=page_pk)
        section_serializer = SectionSerializer(data=request.data)
        if section_serializer.is_valid():
            section_serializer.save()
            pageform_data = {
                "form" : form_pk,
                "page" : page_pk,
                "section" : section_serializer.data["id"]
            }
            pageform = PageFormSerializer(data=pageform_data)
            if pageform.is_valid():
                pageform.save()
                msg = {"message":"Done"}
                stu = status.HTTP_200_OK
            else:
                msg = pageform.errors
                stu = status.HTTP_400_BAD_REQUEST            
        else:
            msg = section_serializer.errors
            stu = status.HTTP_400_BAD_REQUEST 
        return Response(msg, status=stu) 
            
    @action(detail=True, methods=['DELETE'])
    def remove_form_from_page(self, request, page_pk, form_pk, section_pk):
        filter_object(type_object="pageform", form=form_pk, page=page_pk, section=section_pk).delete()
        get_object(type_object="section", primary_key=section_pk).delete()
        return Response("ok", status=200)
        
    @action(detail=True, methods=['GET'])
    def show_page_details(self, request, pk=None):
        page = PageSerializer(get_object(type_object="page", primary_key=pk)).data
        forms_id = page.pop("forms")
        print(page)
        forms = []
        for form_id in forms_id:
            form = FormSerializer(get_object(type_object="form", primary_key=form_id)).data
            form_field = filter_object(type_object="formfield", form=form_id)
            form_field_data = FormFieldSerializer(form_field, many=True) #all form fields
            fields = []
            for field in form_field_data.data:
                field.pop("form")
                id = field.pop("field")
                field_type = FieldSerializer(get_object(type_object="field", primary_key=id)).data["field_type"]
                field["field_type"] = field_type
                fields.append(field)
            form["fields"] = fields
            forms.append(form)
        page["forms"] = forms

        return Response(page, status=200)

class AnswerView(viewsets.ViewSet):

    @action(detail=True, methods=['POST'])
    def set_answer(self, request):
        data = request.data
        page_id = data["id"]
        page = get_object(type_object="page", primary_key=page_id)
        page_data = {
            "page" : page_id,
            "user" : user
        }
        submission = SubmissionSerializer(data=page_data)
        if submission.is_valid():
            answers = data["answers"]
            if answers is not None:
                form_id = answers[0]["form"]
                required_list = list_required_field(form_id=form_id)
                check_list = checking_requirement(requied_field=required_list, answers=answers)
                if not check_list:
                    submission.save()
                    for answer in answers:
                        answer['submission'] = submission.data["id"]
                        ans = AnswerSerializer(data=answer)
                        if ans.is_valid():
                            ans.save()
                        else:
                            filter_object(type_object="submission", id=submission.data["id"]).delete()
                            return Response(ans.errors, status=INVALID_DATA)           
                else:
                    return Response({"message" : "you didn't answer required fileds",
                                     "fields" : check_list}, status=INCOMPLETE_DATA)
        else:
            return Response(submission.errors, status=INVALID_DATA)
        

        return Response()
        


