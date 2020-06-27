from apps.operations.models import UserAsk
from django import forms
class AddAskForm(forms.ModelForm):
    # 进行表单电话的验证
    mobile = forms.CharField(max_length=11, min_length=11, required=True)
    class Meta:
        model = UserAsk
        # 过滤显示的字段
        fields = ["name", "mobile", "course_name"]

