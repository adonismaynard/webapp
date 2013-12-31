import psycopg2
import cgi
def getmovieinfo(cdcode):
    constr = """
       dbname='maynarddb'
       user='maynard'
       password='maynard123'
       host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("""
            select tblcdetail.cdcode,
            tblcdetail.movietitle,
            tblcat.genre, tblcdetail.copyright,
            tblcdetail.availability, tblcdetail.petsa,
            tblcdetail.rentfee
            from tblcdetail, tblcat
            where tblcat.gencode=tblcdetail.gencode and
            tblcdetail.cdcode = """ + str(cdcode))
    rows = curr.fetchall()
    return rows[0]

def index(req, cdcode):
    cdcode = cgi.escape(cdcode)
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
    bodybegin = """
       </head>
       <body>
       <div class="container theme-showcase">
       <div class="jumbotron">
        <h1>Movie Details</h1>
        <table><tr>
        <td><a href="addcd.py" type="button" class="btn btn-lg btn-default">Add CDs</a></td>
        <td><a href="transaction.py" type="button" class="btn btn-lg btn-primary">CD Transactions</a></td>
        <td><a href="rentedlist.py"  type="button" class="btn btn-lg btn-success">Rented List</a></td>
        <td><a href="returned.py" type="button" class="btn btn-lg btn-info">Returned List</a></td>
        <td><a href="customerform.py" type="button" class="btn btn-lg btn-warning">Customer List</a></td>
        <td><a href='genre.py' type="button" class="btn btn-lg btn-danger">Add Genre</a></td></tr></table></center>
        </div>
        </div>
    """
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="bootstrap/js/bootstrap.min.js"></script>
           </body>
           </html>
    """
    movie = getmovieinfo(cdcode)
    moviecontainer = '<div class="container"> '
    moviecontainer += ' <div class="navar-header"> <div class="alert alert-info">'
    moviecontainer +=  ' <h1>Title: '+movie[1]+'</h1> '
    moviecontainer +=   '<p class="panel-body">Genre:' + movie[2] + ' <br>'
    moviecontainer +=   '<p class="panel-body">Copyright Year:' + str(movie[3]) + ' <br>'
    moviecontainer +=   '<p class="panel-body">Availability:' + str(movie[4]) + ' <br>'
    moviecontainer +=   '<p class="panel-body">Date Entry:' + str(movie[5]) + ' &nbsp;'
    moviecontainer +=   '<p class="panel-body">Rental Fee:' + str(movie[6]) + ' <br></div>'
    moviecontainer += '<br /> <a href="http://pythonista.learning.edu/~maynard/index.py"'
    moviecontainer += 'class="btn btn-success btn-sm active">Main Page</a></p></div></div>'

    return header + bodybegin  + moviecontainer + bodyend