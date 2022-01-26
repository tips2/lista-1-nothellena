# **Implementação: Questão 2 - AB1**

O presente projeto apresenta motores de inferência com soluções baseadas em encadeamento
para trás, para frente e misto.

## **Sobre a linguagem da base de conhecimento**

Nas bases de conhecimento, regras e fatos são representados em caixa alta,
confome os seguintes padrões:

### **Regras**

As declarações devem iniciar com a palavra `RULE`, seguida dos termos da premissa,
no formato `INFORMAÇAO=VALOR`, separadas por vírgula. Após a premissa, deve ser utilizada a
a palavra `THEN` para iniciar a conclusão, seguida do termo da conclusão no mesmo 
formato `INFORMAÇAO=VALOR`.

Por exemplo, a regra `SE Dor de cabeça = Sim E Garganta inflamada = Sim E Tosse = Sim
ENTÃO Diagnóstico = Gripe` pode ser representada da seguinte forma:

```
RULE DOR_DE_CABEÇA=SIM GARGANTA_INFLAMADA=SIM TOSSE=SIM THEN DIAGNÓSTICO=GRIPE
```

### **Fatos**

As declarações de fatos devem ser iniciadas com a palavra `FACT` seguidas de um ou mais fatos,
no formato `INFORMAÇÃO=VALOR`, separados por espaços. Desse modo,

```
FACTS A=SIM B=NAO
```
e
```
FACTS A=SIM
FACTS B=SIM
```

são equivalentes.

Para fatos do tipo `fulano TEM diabetes E IMC alto`, a palavra `HAS` deve ser utilizada
, como no exemplo a seguir:

```
FACTS FULANO TEM DIABETES=SIM IMC=ALTO
```

Que, de forma análoga ao anterior, também pode ser escrito como:

```
FACTS FULANO HAS DIABETES=SIM 
FACTS FULANO HAS IMC=ALTO
```

## **Execução**

Para executar inferências, basta executar os comandos abaixo, utilizando
o caminho para o arquivo da base de conhecimento desejada.

**Encadeamento para trás**
```
python3 backward.py <caminho_da_base_de_conhecimento>
```
**Encadeamento para frente**
```
python3 forward.py <caminho_da_base_de_conhecimento>
```

**Encadeamento misto**
```
python3 misto.py <caminho_da_base_de_conhecimento>
```