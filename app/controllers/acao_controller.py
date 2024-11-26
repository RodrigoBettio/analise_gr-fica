from flask import Blueprint, render_template, request
from app.models.acao_model import obter_dados_acoes, obter_dados_commoditys

acao_bp = Blueprint('acao', __name__)

@acao_bp.route("/", methods=["GET", "POST"])
def index():
    grafico_acoes = None
    grafico_commoditys = None
    acao = None
    commodity = None
    data_inicial = None
    data_final = None

    if request.method == "POST":
        # Verifica se o formulário tem dados para Ação
        acao = request.form.get("acao")
        commodity = request.form.get("commodity")
        data_inicial = request.form.get("data_inicial") 
        data_final = request.form.get("data_final") 
        
        if acao:
            grafico_acoes = obter_dados_acoes(acao, data_inicial, data_final) 

        if commodity:
            grafico_commoditys = obter_dados_commoditys(commodity, data_inicial, data_final)

    return render_template(
        "index.html",
        grafico_acoes=grafico_acoes,
        grafico_commoditys=grafico_commoditys,
        acao=acao,
        commodity=commodity,
        data_inicial=data_inicial, 
        data_final=data_final
    )
