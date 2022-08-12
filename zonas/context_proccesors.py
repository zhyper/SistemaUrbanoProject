from .models import PlanEtapa

def get_etapas_plan_links(request):
    etapas = PlanEtapa.objects.all()

    return {
        "etapas_plan": etapas
    }