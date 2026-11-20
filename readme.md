# flask + venv + ios (ddlog + moya)

## ios

### 安装依赖

```
  pod 'CocoaLumberjack'
  pod 'Moya'
```

### moya上传日志

```
[DDLog addLogger:[FlaskLog shared]];
- (void)logMessage:(DDLogMessage *)logMessage{
    NSString *msg = logMessage.message;
    if (msg != nil){
        [FlaskLogProvider sendLogWith_msg:msg];
    }
}
```

## flask日志

### 安装依赖

pip install flask-sqlalchemy

### db初始化

```
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5
DEBUG = True

db = SQLAlchemy()
```

```
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = config.SQLALCHEMY_COMMIT_ON_TEARDOWN
db.init_app(app)
```

### 日志api

```
log_bp = Blueprint("app_log",__name__)

@log_bp.route('/log/', defaults={'msg': 'index'})
@log_bp.get('/log/<msg>')
def robots(msg) :
new_message = message.Message()
new_message.content = str(msg)
new_message.insert()
return render_template('index.html')
```
