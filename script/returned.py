import psycopg2

def cdonrent():
    constr = """
        dbname='maynarddb'
        user='maynard'
        password='maynard123'
        host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("""
                 SELECT tblcdetail.cdcode,
                 tblcdetail.movietitle as returned_cds,
                 tblcustomer.fname,
                 tblcustomer.mname,
                 tblcustomer.lname,
                 tbltransaction.petsa as Date_Returned
                 FROM tblcdreturned,
                 tbltransaction,
                 tblcdetail,
                 tblcustomer
                 WHERE tblcdreturned.cid=tblcustomer.cid and
                 tblcustomer.cid=tbltransaction.cid and
                 tblcdreturned.cdcode=tbltransaction.cdcode and
                 tbltransaction.cdcode=tblcdetail.cdcode and
                 tbltransaction.services='returned'
                 """)
    rows = curr.fetchall()
    return rows

def index(req):
    header = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport"
    content="width=device-width,
    initial-scale=1.0"><meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">
    <title>Using Bootstrap Template</title>
    <!-- Bootstrap core CSS -->
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
    <!-- Bootstrap theme -->
    <link href="bootstrap/css/bootstrap-theme.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="bootstrap/css/theme.css" rel="stylesheet">
    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script
    src="../../docs-assets/js/ie8-responsive-file-warning.js">
    </script><![endif]-->
    <!-- HTML5 shim and Respond.js IE8 support of HTML5
    elements and media queries -->
    <!--[if lt IE 9]>
    <script src="bootstrap/js/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js">
    </script>
    <![endif]-->
    """
    bodybegin="""
        </head>
        <body>
        <div class="container theme-showcase">
        <!-- Main jumbotron for a primary
        marketing message or call to action
        -->
        <div class="jumbotron">
        <h1>Maynard Movies For Rent</h1>
        <p>Returned List </p>
        <p>
        <a href="http://pythonista.learning.edu/~maynard/index.py" class="btn btn-primary btn-lg"
        role="button">Main Page &raquo;</a></p>
        </div>
        <center>
        <p>
         <table><tr>
        <td><a href="addcd.py" type="button" class="btn btn-lg btn-default">Add CDs</a></td>
        <td><button type="button" class="btn btn-lg btn-primary">CD Transactions</button></td>
        <td><a href="rentedlist.py"  type="button" class="btn btn-lg btn-success">Rented List</a></td>
        <td><a href="returned.py" type="button" class="btn btn-lg btn-info">Returned List</a></td>
        <td><a href="customerform.py" type="button" class="btn btn-lg btn-warning">Customer List</a></td>
        <td><a href='genre.py' type="button" class="btn btn-lg btn-danger">Add Genre</a></td></tr></table>
      </p></center>"""
    bodyend = """
        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
        <script src="../../dist/js/bootstrap.min.js"></script>
        <script src="../../docs-assets/js/holder.js"></script>
        </body>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://code.jquery.com/jquery.js"></script>
        <!-- Include all compiled plugins (below), or include
        individual files as needed-->
        <script src="js/bootstrap.min.js"></script>
        </body>
        </html>
        """
    panelbegin = """
        <div class="panel panel-default">
        <!-- Default panel contents -->
        <div class="panel-heading">Returned CDs</div>
        <div class="panel-body">
        """
    tablebegin = """<table class="table table-hover table-condensed">"""
    tableend = "</table>"
    panelend = """
       </div>
      </div>
      """
    movies = cdonrent()
    tablecontents = ""
    tablecontents +="""<tr><th>Movie Title</th>
    <th>First Name</th>
    <th>Middle Name</th><th>Last Name</th><th>Date Returned</th></tr>"""
    i = 1
    for movie in movies:
        if i % 2 == 0:
            class_ = 'class="warning"'
        else:
            class_=""
        tablecontents += "<tr "+class_+">"
        tablecontents += '<td>'+movie[1]+"</td>"
        tablecontents += '<td>'+movie[2]+"</td>"
        tablecontents += '<td>'+movie[3]+"</td>"
        tablecontents += '<td>'+movie[4]+"</td>"
        tablecontents += '<td>'+str(movie[5])+"</td>"
        tablecontents += "</tr>"
        i = i + 1
    return header + bodybegin + panelbegin + tablebegin + tablecontents + tableend + panelend + bodyend
