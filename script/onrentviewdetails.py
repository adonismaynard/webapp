import psycopg2
import cgi
def getmovieinfo(cdcode,cid):
    constr = """
       dbname='maynarddb'
       user='maynard'
       password='maynard123'
       host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("""
                 select tblcustomer.cid,tblcdonrent.petsa,
                 tblcdetail.movietitle as rented_cds,
                 tbltransaction.borroweddisc,
                 tblcustomer.fname,tblcustomer.mname, tblcustomer.lname
                 FROM tblcdonrent,
                 tbltransaction,
                 tblcdetail,
                 tblcustomer,
                 tblcat
                 WHERE tblcdonrent.cid=tblcustomer.cid and
                 tblcustomer.cid=tbltransaction.cid and
                 tblcdonrent.cdcode=tbltransaction.cdcode and
                 tbltransaction.cdcode=tblcdetail.cdcode and
                 tbltransaction.services='rent' and
                 tbltransaction.petsa=tblcdonrent.petsa and
                 tblcdetail.gencode=tblcat.gencode and
                 tblcdetail.cdcode = """
                 + str(cdcode) + """ and
                 tblcustomer.cid ="""
                 + str(cid)+ """""")
    rows = curr.fetchall()
    return rows[0]

def index(cdcode,cid):
    cdcode = cgi.escape(cdcode)
    cid = cgi.escape(cid)
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
        <h1>Renter Details</h1>
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
    movie = getmovieinfo(cdcode,cid)
    moviecontainer = '<div class="container"> '
    moviecontainer += ' <div class="navar-header"> <div class="alert alert-info">'
    moviecontainer +=  ' <h1>Date Rented: '+str(movie[1])+'</h1> '
    moviecontainer +=   '<h2 class="panel-body">Movie Title:' + movie[2] + ' </h2>'
    moviecontainer +=   '<h3 class="panel-body">No. of Disc Borrowed:' + str(movie[3]) + '</h3> '
    moviecontainer +=   '<h4 class="panel-body">Borrower Name:' + movie[4] + '&nbsp;' + movie[5] + '&nbsp;' + movie[6] + ' </h4><br> </div>'
    moviecontainer += '<br /> <a href="http://pythonista.learning.edu/~maynard/index.py"'
    moviecontainer += 'class="btn btn-success btn-sm active">Main Page</a></p></div></div>'

    return header + bodybegin  + moviecontainer + bodyend