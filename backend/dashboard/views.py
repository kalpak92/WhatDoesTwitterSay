# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dashboard.utils.twitter_utils import get_tweets

# Create your views here.

class Search(APIView):
  def post(self, request):
    query = request.POST.get("query")
    data = {
      "tweets": get_tweets(query)
    }
    return Response(data)