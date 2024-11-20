from django.contrib import admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ['user_type','email','first_name','last_name','middle_name','contact','password','gender','dob','is_verified','is_email_verified',]
    list_display = ['id','email','first_name','last_name','middle_name','user_type','contact','gender','dob','is_email_verified','is_staff','is_admin',"created_at","updated_at"]
    search_fields = ['id','email','first_name','last_name','contact']
    list_filter = ['user_type']