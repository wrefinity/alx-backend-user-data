#!/usr/bin/env python3
""" Authentication class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    API authentication classes
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        check if a request is authenticated or not
        Args:
            - path(str): Url to be checked
            - excluded_paths(List of str): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns authorized header from a request object
        """
        if request is None:
            return None
        header_req = request.headers.get('Authorization')
        if header_req is None:
            return None
        return header_req

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return the current user
        """
        return None
