import 'package:flutter_test/flutter_test.dart';
import '../../lib/domain/pedido.dart';
import '../../lib/domain/produto.dart';

void main () {

  test('deve adicionar produtos no pedido', () {
    Produto produto = Produto(10, 'Monitor', 999.90);
    Produto produto2 = Produto(12, 'TV', 99.90);

    Pedido pedido = Pedido('Renan');

    pedido.addProduto(produto);
    pedido.addProduto(produto2);

    Produto menorValor = pedido.produtos.reduce((a, b) => a.valor < b.valor ? a : b);

    expect(pedido.produtos.length, 2);
    expect(menorValor, 99.90);
    expect(pedido.produtos[0].valor, 999.90);
    expect(pedido.produtos[1].valor, 99.90);
  });

  test('deve remover produtos no pedido', () {
    Produto produto = Produto(10, 'Monitor', 999.90);
    Produto produto2 = Produto(12, 'TV', 99.90);

    Pedido pedido = Pedido('Renan');

    pedido.addProduto(produto);
    pedido.addProduto(produto2);

    pedido.removerProduto(produto);

    expect(pedido.produtos[0].valor, 99.90);
  });
}