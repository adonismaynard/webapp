import psycopg2
import cgi

def adgen(fname,mname,lname,street,purok,brgyname):
    connection = """
    dbname='maynarddb'
    user='maynard'
    password='maynard123'
    host='pythonista.learning.edu'
    """
    conns = psycopg2.connect(connection)
    currs = conns.cursor()
    currs.execute("""
    insert into tblcustomer (fname,mname,lname,street,purok,brgyname) values ('"""+str(fname)+"""','"""
    +str(mname)+"""','"""+str(lname)+"""','"""+str(street)+"""','"""+str(purok)+"""','"""+str(brgyname)+"""')
    """)
    conns.commit()
def index(req,fname,mname,lname,street,purok,brgyname):
    header = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <META http-equiv="refresh" content="2;URL=customerform.py">
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
        </head><body><h1 class='alert alert-danger'>Customer's' Name just been added.
        </h1>
        """
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

    result= adgen(fname,mname,lname,street,purok,brgyname)
    result = '<div class="container"> '
    result += ' <div class="navar-header"> <div class="alert alert-info">'
    result +=  ' <h1>Date Rented: '+ str( result )+'</h1> '

    return header + bodybegin + bodyend
