# 📉 Churn Prediction — Projeto End-to-End (IA + Dados)

## 1. Contexto e Problema de Negócio

A retenção de clientes é um dos principais desafios em empresas de telecomunicações.  
Perder clientes (churn) impacta diretamente receita, custo de aquisição e crescimento.

**Pergunta central do projeto:**

> *Quais clientes têm maior probabilidade de cancelar o serviço e como priorizar ações de retenção de forma eficiente?*

O foco não é apenas prever churn, mas **apoiar uma decisão real de negócio**:  
atuar em um subconjunto limitado de clientes com maior risco.

---

## 2. Dataset

- **Fonte:** Telco Customer Churn (Kaggle)
- **Granularidade:** Cliente
- **Tamanho:** ~7.000 registros
- **Variável target:** `Churn`
  - `Yes` → cliente cancelou
  - `No` → cliente permaneceu

### Principais tipos de variáveis
- Perfil do cliente (gênero, senioridade, dependentes)
- Serviços contratados (internet, streaming, suporte)
- Contrato e forma de pagamento
- Cobrança mensal e total

---

## 3. Definição do Problema Analítico

- **Tipo:** Classificação binária
- **Classe de interesse:** Churn = 1
- **Métrica principal:** **Recall da classe churn**

**Justificativa:**

> É mais crítico **não deixar um cliente que vai cancelar passar despercebido**, mesmo ao custo de algumas ações desnecessárias.

---

## 4. Pipeline do Projeto

### 4.1 ETL
- Leitura dos dados brutos
- Padronização de tipos
- Encoding de variáveis categóricas (`get_dummies`)
- Separação clara entre:
  - features
  - target
- Pipeline reproduzível

---

### 4.2 Feature Engineering
- Encoding one-hot para variáveis categóricas
- Remoção de identificadores sem valor preditivo
- Seleção de features baseada em **importância do modelo**

> A seleção foi usada para reduzir ruído e manter interpretabilidade.

---

### 4.3 Modelagem

- **Modelo:** Decision Tree Classifier
- **Motivos da escolha:**
  - Interpretável
  - Fácil explicação em contexto de negócio
  - Boa baseline para churn

**Hiperparâmetros:**
- `max_depth = 4`
- `min_samples_leaf = 20`

**Separação treino/teste:**
- 80% treino
- 20% teste

---

## 5. Avaliação do Modelo

Avaliação realizada **exclusivamente no conjunto de teste**.

### Resultados principais (classe Churn = 1):
- **Recall ≈ 53%**
- **Precision ≈ 66%**
- **Accuracy ≈ 80%**
- **ROC-AUC** utilizado para avaliar qualidade do ranking

**Interpretação:**

> O modelo identifica cerca de **53% dos clientes que realmente iriam cancelar**, mantendo precisão razoável.

---

## 6. Geração de Churn Score

Em vez de apenas classificar clientes como `0/1`, o modelo gera:

- **Churn Score:** probabilidade de cancelamento ∈ [0,1]

Esse score permite:
- ranking de clientes
- priorização de ações
- simulação de cenários reais

---

## 7. Simulação de Decisão de Negócio

### Regra simulada
> A empresa só consegue atuar em **20% da base** (restrição operacional).

### Processo
1. Clientes ordenados por churn score (decrescente)
2. Seleção do top 20%
3. Medição da proporção de churns reais capturados

### Resultado
> Atuando em apenas **20% dos clientes**, é possível capturar uma **parcela significativa dos churns reais**, demonstrando ganho operacional em relação a uma ação aleatória.

Este passo transforma o modelo em **ferramenta de decisão**, não apenas previsão.

---

## 8. Output Final

O projeto gera um dataset final (`churn_output.csv`) contendo:

- `customerID`
- `churn_score`
- `churn_real`
- `faixa_risco` (Baixo / Médio / Alto)

Esse arquivo é o **input direto para dashboards e áreas de negócio**.

---

## 9. Visualização (Power BI)

O output foi preparado para visualização em Power BI, com foco em:

1. **Visão de negócio**
   - Taxa de churn
   - Churn por tipo de contrato e serviço

2. **Modelo**
   - Métricas principais
   - Performance geral

3. **Ação**
   - Clientes de alto risco
   - Simulação de priorização (20%)

---

## 10. Limitações

- Modelo simples (Decision Tree)
- Não há tuning extensivo de hiperparâmetros
- Não considera custo financeiro explícito das ações
- Dataset estático (não temporal)

Essas limitações são **intencionais**, priorizando clareza e domínio de fundamentos.

---

## 11. Próximos Passos

- Comparar com modelos ensemble (Random Forest / Gradient Boosting)
- Ajustar threshold visando maximizar recall
- Incorporar custo de retenção vs perda de cliente
- Evoluir para versionamento e monitoramento (ex: MLflow)

---

## 12. Conclusão

Este projeto demonstra um fluxo **end-to-end de IA aplicada a dados**, indo além da modelagem:

> O foco foi transformar dados em **priorização de decisão**, com métricas e outputs alinhados ao negócio.
