from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import re

# validação de nome
def validate_full_name(valor):
    if not re.match(r'^[A-Za-z\s\-\'\.]+$', valor):
        raise ValidationError("Nome contém caracteres inválidos.")

# validação para garantir que data de nascimento não seja no futuro.    
def validar_data_nascimento(valor):
   
        if valor > timezone.now().date():
            raise ValidationError("A data de nascimento não pode estar no futuro.")

# validação de endereço       
def validate_address(valor):
    if not re.match(r'^[A-Za-z0-9\s\-,]+$', valor):
        raise ValidationError("Endereço contém caracteres inválidos.")


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100, validators=[validate_full_name])
    data_nascimento = models.DateField(validators=[validar_data_nascimento])
    endereco = models.CharField(max_length=200, validators=[validate_address])
    cpf = models.CharField(max_length=11, unique=True, verbose_name=_('CPF'))
    ESTADO_CIVIL = (
    ('solteiro', 'Solteiro'),
    ('casado', 'Casado'),
    ('divorciado', 'Divorciado'),
    ('viuvo', 'Viuvo'),
    )
    estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL)


    # validação de cpf
    def clean(self):
        cpf = self.cpf
        if not cpf.isdigit() and len(cpf) != 11:
            raise ValidationError(_('CPF deve conter 11 digitos.'))
   

    def __str__(self):
        return self.nome_completo