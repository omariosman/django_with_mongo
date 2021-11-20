from django import forms
from .models import Program, Instruction

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name']

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['program','type', 'var', 'inst']



class ChooseProgramForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['program']
    