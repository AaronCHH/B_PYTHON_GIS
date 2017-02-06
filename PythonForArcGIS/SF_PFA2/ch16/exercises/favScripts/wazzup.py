import os, sys

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.dirname(scriptPath)
relativePath = '../'
modulePathA = os.path.join(scriptDir, relativePath)
sys.path.append(modulePathA)
import scriptA
