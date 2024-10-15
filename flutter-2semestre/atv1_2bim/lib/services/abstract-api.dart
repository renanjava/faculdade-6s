import 'dart:convert';

import 'package:http/http.dart' as http;

abstract class AbstractApi<T> {
    Future<List<T>> getAll();
    Future<T> getById(String id);
    Future<T> post(String id);
    Future<T> patch(String id);
    Future<void> delete(String id);
}