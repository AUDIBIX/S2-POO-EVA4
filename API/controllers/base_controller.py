from flask import Blueprint, jsonify
from typing import Any, Tuple, Dict, Union
from http import HTTPStatus

class BaseController:
    def __init__(self):
        self._status = HTTPStatus
    
    def _success_response(self, 
                         data: Union[Dict, list, None] = None, 
                         status: int = HTTPStatus.OK) -> Tuple[Any, int]:
        """Standard success response"""
        if data is None:
            return '', status
        return jsonify(data), status
    
    def _error_response(self, 
                       message: str, 
                       status: int = HTTPStatus.BAD_REQUEST) -> Tuple[Any, int]:
        """Standard error response"""
        return jsonify({"error": message}), status
    
    def _successResponse(self, data=None, status=HTTPStatus.OK):
        response = {
            'status': 'success',
            'data': data
        }
        return jsonify(response), status 