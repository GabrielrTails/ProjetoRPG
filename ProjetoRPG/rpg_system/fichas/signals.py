from django.db.models.signals import post_save
from django.dispatch import receiver
from fichas.models import Ficha
from combate.models import FichaCombate

@receiver(post_save, sender=Ficha)
def criar_ficha_combate(sender, instance, created, **kwargs):
    if created and not instance.ficha_combate:  # Verifica se já não há ficha de combate associada
        combate = FichaCombate.objects.create(
            usuario=instance.usuario,
            ficha_base=instance,
            vida=instance.atributos.get('vida', 100),  # Atributos padrão
            mana=instance.atributos.get('mana', 50),
            atributos=instance.atributos,
            barras_personalizaveis={},
            dados={},
            anotacoes=""
        )
        # Atualiza e salva a relação na ficha base
        instance.ficha_combate = combate
        instance.save()