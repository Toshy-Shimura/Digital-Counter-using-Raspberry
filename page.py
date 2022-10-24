class HTMLPAGE(object):
  def __init__(self, counter):
    self.counter = counter
    
  def page(self):  

    self.html = """<!DOCTYPE HTML><html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
      <style>
        html {
         font-family: Arial;
         display: inline-block;
         margin: 0px auto;
         text-align: center;
        }
        h2 { font-size: 2.0rem; }
        p { font-size: 2.0rem; }
        .units { font-size: 1.2rem; }
        .bme-labels{
          font-size: 1.5rem;
          vertical-align:middle;
          padding-bottom: 15px;
        }
      </style>
    </head>
    <body>
    <script>setTimeout(()=>document.location.reload(), 3000)</script>
      <h2>Counter using Raspberry Pi Pico W</h2>
      <p>
        <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
        <span class="bme-labels">Cuenta:</span> 
        <span>"""+str(self.counter)+"""</span>
      </p>

    </body>
    </html>
    """
    return self.html