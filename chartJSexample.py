# chartJSexample.py

from browser import document, html, alert, window

try:
    # Prepare data for chart    
    cTitle = 'My Title'
    cTheme = 'light2'   # Change to: 'light1', 'light2', 'dark1', 'dark2', etc.
    cType = 'bar'       # Change to: 'column', 'bar', 'area', 'spline", 'pie', etc.
    cAnim = False
    cData = []
    cLabels = ['apples','beetroot','carrots','damsel','elderberry']
    cPoints = [10, 40, 20, 50, 30.6]

    # Show chart
    window.doChart(cTitle, cTheme, cType, cAnim, cLabels, cPoints)

except Exception as err:
    alert('Python Exception: ' + str(err))

