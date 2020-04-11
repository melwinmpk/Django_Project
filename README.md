# Django_Project (TestTakers)
  Test Takers is a web site for the students to take the test and get to know about their marks. Teachers can login and create new subjects and add Questions to it.(Developed in Django)
<div>
    <h2>Screenshots and Link</h2>
    <h3>Screenshots = https://github.com/melwinmpk/Django_Project/blob/master/Screenshorts.md</h3>
    <h3>Link = https://testtakersweb.herokuapp.com/</h3>
    <h2>Buisness Logic</h2>
    <h3>Students Work Flow</h3>
      <ul>
          <li>First Students should have an account to take a test Students can register their account in the website itself after logging in students can take their test</li>
          <li>Students has to select the Subjects which he has to take test.</li>
      </ul>
    <h3>Teacher Work Flow</h3>
        <ul>
            <li>Only Teacher/Super Admin can add/Create Questions A teacher should have an account to add/Create a question. </li>
            <li>The Teachers Account is created by the super Admin from Back End. Before Adding/Creating a question. </li>
            <li>The Question must be linked to a Subject A subject can be created by a Teacher in the website itself. </li>
            <li>Question type must also be selected while adding a question Question type creation is done by Super User from back end only.</li>
        </ul>
</div>
<div>
    <h2>System Set Up</h2>
    <ul>
        <li><b>PreRequisite:</b>Django should have been already installed in a particular environment</li>
        <li><b>PreRequisite:</b>In this Project, I used PostGresSQL so those setups have used been already installed</li>
        <li>Clone the Project to the respective directory</li>
        <li>In this project Postgres is used So change the host, password, Username, DatabaseName accordingly</li>
        <pre>
        'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                        'NAME': 'db_name', #DATABASE_NAME
                        'USER': 'user_name',
                        'PASSWORD': 'your_password',
                        'HOST': 'localhost'
                    }
        </pre>
        <li>We will be requiring a connector for the PostgreSQL to connect to the python</li>
        <pre>pip install psycopg2</pre>
        <li>Set the static folder</li>
        <pre>python manage.py collectstatic</pre>
        <li>By default, the static folder will be created in the name of assets(Django which creates) and Static_content you can change the location in settings.py</li>
        <li>For Migeration run commands</li>
        <pre>python manage.py makemigrations</pre>
        <pre>python manage.py migrate</pre>
        <li>Create the super User for back end and create a user for the Teacher in backend</li>
        <pre>python manage.py createsuperuser</pre>
    </ul>
</div>
