import arcgisscripting
import os
import sys
import types
import locale
gp = arcgisscripting.create(9.3)

#Define l"aBssag-e C012stant .s 50 t12ey. may })e t. 1.:a12s1ated easily
msgBufferRings = gp.GetIDMessage(86149)  # HB 'L ~ffe J_ 'inç/ distance rr
msgMergeRings = gp.GetIDMessage(86150)   # Hj\fe;:_'çring" 1: . . rr
msgDissolve = gp.GetIDMessage(86151)     #"Dissolving' ve.rl a.p'p.1 12g" })Ol~ da ì.'.1 BS . . rf
def initiateMultiBuffer():
# Get the input argument values
# Input FC
input
# Output FC
output
# Distances
distances
# Unit
= gp.GetParameterAsText(
= gp.GetParameterAsText( l )
= gp.GetParameter( 2 )
un l. t =的. GetParar ，時 terAsText(
主主 unit.l 。可 rer () == "de ault"
unit ;::; Hrr
120 field naIae .1 5 specif.1 ed, use t12ð 12az "distance by' default
ieldName = chec k: Fielc larne (gp , gp. GetParameterAsText (4 ) , s.path.dirn 前時 (output) )
#Diss lve opt~on
dissolveOption = gp.GetParameterAsText( 5 )
# Outsi d. e Poly~...ons
outsidePolygons = gp.GetPararneterAsText( 6 )
outsidePolygons.lower() == "true" :
sideType = "OUT3IDE ONLY"
e1se :
sideType = ""
createMultiBu 主主 ers(gp input , output , distances , unit , 主工 ldName , diss lveOption sideType)