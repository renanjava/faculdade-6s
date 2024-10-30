class Produto {
    String nome;
    double valor;

    Produto(required this.nome, required this.valor);

    factory Produto.fromJson(Map<String, dynamic> objJson) {
        return Produto(nome: objJson["nome"], valor: objJson["valor"]);
    }
}