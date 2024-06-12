"""
This is a test module for the handelsregister package.
"""

import argparse
import pytest
from handelsregister import get_companies_in_searchresults, HandelsRegister


def test_parse_search_result():
    """
    Test the parsing of search results.
    """
    # simplified html from a real search
    html = '<html><body>%s</body></html>' % """<table role="grid"><thead></thead><tbody id="ergebnissForm:selectedSuchErgebnisFormTable_data" class="ui-datatable-data ui-widget-content"><tr data-ri="0" class="ui-widget-content ui-datatable-even" role="row"><td role="gridcell" colspan="9" class="borderBottom3"><table id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt147" class="ui-panelgrid ui-widget" role="grid"><tbody><tr class="ui-widget-content ui-panelgrid-even borderBottom1" role="row"><td role="gridcell" class="ui-panelgrid-cell fontTableNameSize" colspan="5">Berlin  <span class="fontWeightBold"> District court Berlin (Charlottenburg) HRB 44343  </span></td></tr><tr class="ui-widget-content ui-panelgrid-odd" role="row"><td role="gridcell" class="ui-panelgrid-cell paddingBottom20Px" colspan="5"><span class="marginLeft20">GASAG AG</span></td><td role="gridcell" class="ui-panelgrid-cell sitzSuchErgebnisse"><span class="verticalText ">Berlin</span></td><td role="gridcell" class="ui-panelgrid-cell" style="text-align: center;padding-bottom: 20px;"><span class="verticalText">currently registered</span></td><td role="gridcell" class="ui-panelgrid-cell textAlignLeft paddingBottom20Px" colspan="2"><div id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt160" class="ui-outputpanel ui-widget linksPanel"><script type="text/javascript" src="/rp_web/javax.faces.resource/jsf.js.xhtml?ln=javax.faces"></script><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:0:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:0:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:0:popupLink" class="underlinedText">AD</span></a><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:1:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:1:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:1:popupLink" class="underlinedText">CD</span></a><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:2:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:2:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:2:popupLink" class="underlinedText">HD</span></a><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:3:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:3:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:3:popupLink" class="underlinedText">DK</span></a><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:4:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:4:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:4:popupLink" class="underlinedText">UT</span></a><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:5:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:5:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:5:popupLink" class="underlinedText">VÖ</span></a><a id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:6:fade" href="#" class="dokumentList" aria-describedby="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:6:toolTipFade"><span id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt161:6:popupLink" class="underlinedText">SI</span></a></div></td></tr><tr class="ui-widget-content ui-panelgrid-even" role="row"><td role="gridcell" class="ui-panelgrid-cell" colspan="7"><table id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt172" class="ui-panelgrid ui-widget marginLeft20" role="grid"><tbody><tr class="ui-widget-content ui-panelgrid-even borderBottom1 RegPortErg_Klein" role="row"><td role="gridcell" class="ui-panelgrid-cell padding0Px">History</td></tr></tbody></table><table id="ergebnissForm:selectedSuchErgebnisFormTable:0:j_idt176" class="ui-panelgrid ui-widget" role="grid"><tbody><tr class="ui-widget-content" role="row"><td role="gridcell" class="ui-panelgrid-cell RegPortErg_HistorieZn marginLeft20 padding0Px" colspan="5"><span class="marginLeft20 fontSize85">1.) Gasag Berliner Gaswerke Aktiengesellschaft</span></td><td role="gridcell" class="ui-panelgrid-cell RegPortErg_SitzStatus "><span class="fontSize85">1.) Berlin</span></td><td role="gridcell" class="ui-panelgrid-cell textAlignCenter"></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>"""
    res = get_companies_in_searchresults(html)
    assert res == [{
            'court': 'Berlin   District court Berlin (Charlottenburg) HRB 44343', 
            'name': 'GASAG AG',
            'state': 'Berlin',
            'status': 'currently registered',
            'documents': 'ADCDHDDKUTVÖSI',
            'history': [('1.) Gasag Berliner Gaswerke Aktiengesellschaft', '1.) Berlin')]
            }]


def test_get_results():
    """
    Test the retrieval of search results.
    """
    args = argparse.Namespace(debug=False, force=False, schlagwoerter='deutsche bahn', schlagwortOptionen='all')
    h = HandelsRegister(args)
    h.open_startpage()
    companies = h.search_company()
    assert len(companies) > 0


import pytest
from handelsregister import get_companies_in_searchresults, HandelsRegister
import argparse