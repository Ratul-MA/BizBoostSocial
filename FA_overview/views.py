from django.http import HttpResponse
from django.shortcuts import render
from .financial_data import FinancialDataManager
from django.conf import settings
from django.contrib.auth.decorators import login_required
import pandas as pd
import os
import requests
import logging


def index(request):
    return render(request, "index.html")


def MyBizBoostProfile(request):
    return render(request, "MyBizBoostProfile.html")


