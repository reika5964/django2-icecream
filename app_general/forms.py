from django import forms
from app_foods.models import Food
from .models import Subscription

class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60,required=True,label='名前')
    email = forms.EmailField(max_length=60,required=True,label='メール')
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,label='好きなフレーバー',
        widget= forms.CheckboxSelectMultiple
        )
    accepted = forms.BooleanField(required=True,label='当社は、収集した個人情報について、以下の目的のために利用いたします。商品・サービス・イベントの案内のため')


class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,label='好きなフレーバー',
        widget= forms.CheckboxSelectMultiple
        )
    accepted = forms.BooleanField(required=True,label='当社は、収集した個人情報について、以下の目的のために利用いたします。商品・サービス・イベントの案内のため')    

    class Meta:
        model = Subscription
        fields =['name','email','food_set','accepted']
        labels= {
            'name': '名前(フールネーム)',
            'email': 'メール',
            'food_set': '好きなフレーバー'
        }
