void main() {

    test('deve retornar um produto', () async {

        MyMockClient mockClient = MyMockClient();

        Uri uri = Uri.parse("http://localhost:3000/produtos");

        when(() => mockClient.get(uri)).thenAnswer((_) async => Response('{"nome": "Teclado", "valor": 89.9}', 200));

        ProdutoService service = ProdutoService();

        Produto resultado = await service.getProduto()

        expect(resultado.nome, 'Teclado');
        expect(resultado.valor, 89.9);
    })
}