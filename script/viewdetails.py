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
            tblcat.genre,
            tblcdetail.availability
            from tblcdetail, tblcat
            where tblcat.gencode=tblcdetail.gencode and
            tblcdetail.cdcode = """ + str(cdcode))
    rows = curr.fetchall()
    return rows[0]

def index(req, cdcode):
    cdcode = cgi.escape(cdcode)
    header = """
	<!DOCTYPE html>
	<html>
	<head>
	<title>Movies Database Example</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- Bootstrap -->
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
	<link href="bootstrap/css/bootstrap-theme.min.css" rel="stylesheet">
	<link href="bootstrap/css/theme.css" rel="stylesheet">
	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
	    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
	    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
	    <![endif]-->
	    """
    bodybegin = """
       </head>
       <body>
       <div class="container theme-showcase">
       <div class="jumbotron">
        <h1>Movie Details</h1>
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
    moviecontainer += ' <div class="starter-template"> '
    moviecontainer +=  ' <h1>Title: '+movie[1]+'</h1> '
    moviecontainer +=   '<p class="lead">Genre:' + movie[2] + ' <br>'
    moviecontainer +=   '<p class="lead">Availability:' + str(movie[3]) + ' <br>'
    moviecontainer += '<br /> <a href="http://pythonista.learning.edu/~maynard/index.py"'
    moviecontainer += 'class="btn btn-success btn-sm active">Main Page</a></p></div></div>'

    return header + bodybegin  + moviecontainer + bodyend