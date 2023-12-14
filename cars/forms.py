from django import forms
from cars.models import Brand, Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  


    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Não é possivel cadastrar carros abaixo de R$20.000')
        return value 
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2015:
            self.add_error('factory_year', 'Não é Possivel cadastrar carros antes de 2015')
        return factory_year
    