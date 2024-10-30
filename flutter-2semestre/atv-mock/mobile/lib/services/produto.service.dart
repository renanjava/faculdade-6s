import 'package:http/http.dart';
import 'package:domain/produto.dart';

class ProdutoService {
    Client client;
    ProdutoService(this.client);

    Future<Produto> getProduto() async {
        Uri uri = Uri.parse("http://localhost:3000/produtos");
        Response response = await client.get(uri);

        if(response.statusCode == 200){
            return Produto.fromJson(jsonDecode(response.body));
        }

        return throw Exception('Erro');
    } 
}
