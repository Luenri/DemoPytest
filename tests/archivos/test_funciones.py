import pytest

from ...archivos.functions import *

def testSuma():
	assert suma(5,3)==8


def testResta():
	assert resta(8,9)==-1