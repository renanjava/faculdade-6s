import 'produto.dart';

class Pedido {
  String nomeCliente;
  List<Produto> produtos;

  Pedido(this.nomeCliente) : produtos = [];

  void addProduto(Produto produto){
    this.produtos.add(produto);
  }

  void removerProduto(Produto produto){
    this.produtos.remove(produto);
  }
}