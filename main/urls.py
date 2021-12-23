
from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('atomic_models', views.atomic_models, name='atomic_models'),
    path('big_bang', views.big_bang, name='big_bang'),
    path('black_holes', views.black_holes, name='black_holes'),
    path('black_body', views.black_body, name='black_body'),
    path('bohrs_mod', views.bohrs_mod, name='bohrs_mod'),
    path('brem_rad', views.brem_rad, name='brem_rad'),
    path('exp_universe', views.exp_universe, name='exp_universe'),
    path('feynman_d', views.feynman_d, name='feynman_d'),
    path('galaxies', views.galaxies, name='galaxies'),
    path('heisenberg_uncertainty', views.heisenberg_uncertainty, name='heisenberg_uncertainty'),
    path('higgs', views.higgs, name='higgs'),
    path('pe_effect', views.pe_effect, name='pe_effect'),
    path('q_comp', views.q_comp, name='q_comp'),
    path('qc_alg', views.qc_alg, name='qc_alg'),
    path('qed', views.qed, name='qed'),
    path('ruth_mod', views.ruth_mod, name='ruth_mod'),
    path('schr_eq', views.schr_eq, name='schr_eq'),
    path('shors_alg', views.shors_alg, name='shors_alg'),
    path('space_time', views.space_time, name='space_time'),
    path('standard_model', views.standard_model, name='standard_model'),
    path('star_form', views.star_form, name='star_form'),
    path('supernovae', views.supernovae, name='supernovae'),
    path('thermonuclear_fus', views.thermonuclear_fus , name='thermonuclear_fus'),
    path('turing_machine', views.turing_machine, name='turing_machine'),
    path('atomic_models', views.atomic_models, name='atomic_models'),
    path('atomic_models', views.atomic_models, name='atomic_models'),
    path('atomic_models', views.atomic_models, name='atomic_models'),
    path('register', views.register_request, name='register'),
    #path('contact_form', views.contact_form, name='contact_form'),
    path('generator', views.generator, name='generator'),
    path('q_teleporation', views.q_teleporation, name='q_teleporation'),
    path('text_field', views.text_field, name='text_field'),
    path('register', views.register, name='register'),
    path('text_algo', views.text_algo, name='text_algo'),
    path('top_menu', views.top_menu, name='top_menu'),
    path('top_menu_no_contact', views.top_menu_no_contact, name='top_menu_no_contact'),
    path('search_results', views.search_results, name='search_results'),
    




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
