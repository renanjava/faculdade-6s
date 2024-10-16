import 'dart:convert';

import 'package:http/http.dart' as http;

abstract class ImplementService<T> {
  final String _urlPath = 'http://localhost:3000';
  final String _resource;

  ImplementService(this._resource);

  Future<List<T>> getAll() async {
    final response = await http.get(Uri.parse('$_urlPath/$_resource'));
    if (response.statusCode == 200) {
      List<dynamic> jsonResponse = json.decode(response.body);
      return jsonResponse.map((data) => fromJSON(data)).toList();
    } else {
      throw Exception('Failed to load data');
    }
  }

  Future<T> create(T item) async {
    final response = await http.post(Uri.parse('$_urlPath/$_resource'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: json.encode(toJSON(item)));

    if (response.statusCode == 201) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to create data');
    }
  }

  Future<void> update(int id, T item) async {
    final response = await http.put(Uri.parse('$_urlPath/$_resource/$id'),
        headers: {
          'Content-Type': 'application/json',
        },
        body: json.encode(toJSON(item)));

    if (response.statusCode != 200) {
      throw Exception('Failed to update data');
    }
  }

  Future<void> delete(String id) async {
    final response = await http.delete(Uri.parse('$_urlPath/$_resource/$id'));

    if (response.statusCode != 200) {
      throw Exception('Failed to delete data');
    }
  }

  T fromJSON(Map<String, dynamic> json);

  Map<String, dynamic> toJSON(T item);
}
