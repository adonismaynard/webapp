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
                 SELECT (tblcustomer.fname,
                 tblcustomer.mname,
                 tblcustomer.lname) as rented_by,
                 tblcdetail.movietitle as rented_cds
                 FROM tblcdonrent,
                 tbltransaction,
                 tblcdetail,
                 tblcustomer
                 WHERE tblcdonrent.cid=tblcustomer.cid and
                 tblcustomer.cid=tbltransaction.cid
                 and tblcdonrent.cdcode=tbltransaction.cdcode and
                 tbltransaction.cdcode=tblcdetail.cdcode and
                 tbltransaction.services='rent' and
                 tbltransaction.petsa=tblcdonrent.petsa
                 """)
    rows = curr.fetchall()
def index(req):
header ="""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport"
            content="width=device-width,
            initial-scale=1.0">
            <meta name="description" content="">
            <meta name="author" content="">
            <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">
            <title>Theme Template for Bootstrap</title>
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
              <script
                src="bootstrap/js/html5shiv.js"></script>
              <script
                src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js">
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
        <p>Your offline movies are here. </p>
        <p>
        <a href="#" class="btn btn-primary btn-lg"
         role="button">Learn more &raquo;</a></p>
          </div>
            <!-- Bootstrap core JavaScript
            ================================================== -->
            <!-- Placed at the end of the document so the pages load faster -->
                <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
                <script src="../../dist/js/bootstrap.min.js"></script>
                <script src="../../docs-assets/js/holder.js"></script>
              </body>"""
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="js/bootstrap.min.js"></script>
           </body>
           </html>
    """


    """




return header + bodybegin