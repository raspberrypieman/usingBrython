# canvasJSexample.py

from browser import document, html, alert, window

def doChart(event):
#try:
    chartTypes = ['column', 'bar', 'pie', 'spline', 'area']
    for n in range(5):
        if document['type' + str(n)].checked:
            cType = chartTypes[n]

    # Prepare data for chart    
    cTitle = 'My Title'
    cTheme = 'light2'   # Change to: 'light1', 'light2', 'dark1', 'dark2', etc.
    #cType = 'bar' #'column'    # Change to: "bar", "area", "spline", "pie", etc.
    cAnim = False
    cData = []
    cLabels = ['apples','beetroot','carrots','damsel','elderberry']
    cPoints = [10, 40, 20, 50, 30.6]

    # Show chart
    window.doChart(cTitle, cTheme, cType, cAnim, cLabels, cPoints)

try:
    # Bind Radio-Buttons
    for n in range(5):
        document['type' + str(n)].bind('click', doChart)
    doChart(None)

except Exception as err:
    alert('Python Exception: ' + str(err))

