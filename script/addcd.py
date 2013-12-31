import psycopg2
import cgi
import datetime
import time

def customershow():
    constr = """
        dbname='maynarddb'
        user='maynard'
        password='maynard123'
        host='pythonista.learning.edu'
    """
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
        <script src="bootstrap/js/respond.min.js">
        </script>
        <![endif]-->
        """
    bodybegin="""
        </head>
        <body>
        <div class="container theme-showcase">
        </div>
        <center>
        <p>
        <table><tr>
        <td><a href="addcd.py" type="button" class="btn btn-lg btn-default">Add CDs</a></td>
        <td><a href="transaction.py" type="button" class="btn btn-lg btn-primary">CD Transactions</a></td>
        <td><a href="rentedlist.py"  type="button" class="btn btn-lg btn-success">Rented List</a></td>
        <td><a href="returned.py" type="button" class="btn btn-lg btn-info">Returned List</a></td>
        <td><a href="customerform.py" type="button" class="btn btn-lg btn-warning">Customer List</a></td>
        <td><a href='genre.py' type="button" class="btn btn-lg btn-danger">Add Genre</a></td></tr></table>
      </p></center>"""
    bodyend = """
        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="bootstrap/js/jquery-1.10.2.min.js"></script>
        <script src="bootstrap/js/bootstrap.min.js"></script>
        <script src="bootstrap/js/holder.js"></script>
        </body>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://code.jquery.com/jquery.js"></script>
        <!-- Include all compiled plugins (below), or include
        individual files as needed-->
        <script src="bootstrap/js/bootstrap.min.js"></script>
        </body>
        </html>
        """
    panelbegin = """
        <div class="panel panel-default">
        <!-- Default panel contents -->
        <div class="panel-heading"><center><h1>NEW MOVIE COPIES</h1>
        <form action='savecd.py'>
        <table><tr><th>Movie Title</th><td><input type='text' name='movietitle'></td></tr>
        <tr><th>Genre</th><td><input type='text' name='gencode'></td></tr>
        <tr><th>Copyright</th><td><input type='text' name='copyrights'></td></tr>
        <tr><th>No. of CD Copies</th><td><input type='text' name='availability'></td></tr>
        <input type='hidden' name='petsa' value="""+str( datetime.date.today())+""">
        <tr><th>Rental Fee</th><td><input type='text' name='rentfee'></td></tr>
        <tr><td colspan='2'> <input type='submit' value='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SAVE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' class="btn btn-lg btn-success">
        <input type='reset' value='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CLEAR&nbsp;&nbsp;&nbsp;&nbsp;' class="btn btn-lg btn-warning"></td></tr>
        </table>
        </form></center>
        <p>
        <a href="http://pythonista.learning.edu/~maynard/index.py" class="btn btn-primary btn-lg"
        role="button">Main Page &raquo;</a></p>
        </div>
        """
    return header+ bodybegin + panelbegin + bodyend
