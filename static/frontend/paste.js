/** @jsx React.DOM */
var PasteForm = React.createClass({
    handleSubmit: function() {
        var paste = this.refs.raw_paste.getDOMNode().value.trim();
        if (!paste) {
            return false;
        }
        this.refs.raw_paste.getDOMNode().value = '';
        return false;
    },
    render: function() {
        return (
            <form className="pasteForm" onSubmit={this.handleSubmit}>
                <textarea placeholder="Enter your code here." ref="raw_paste"></textarea>
                <input type="submit" value="Post"/>
            </form>
            );
    }
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


var PasteBox = React.createClass({
    loadPasteFromServer: function() {
        var csrftoken = getCookie('csrftoken'); // required by django rest
        $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: this.props.url,
            dataType: 'json',
            success: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    handlePasteSubmit: function(paste) {
        console.log('pasting...');
        var pastes = this.state.data;
        this.setState({'code': paste, 'display_linenos':true, 'language':'python', 'style':'default', 'title':'Hello, Code Comment!'});
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            type: 'POST',
            data: this.state.data,

            success: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function() {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadPasteFromServer();

    },
  render: function() {
    return (
      <div className="pasteBox">
      <h1>Pastes</h1>
        <PasteForm onPasteSubmit={this.handlePasteSubmit} />
      </div>
    );
  }
});


React.renderComponent(
    <PasteBox url="api/snippets/" />,
    document.getElementById('content')
    );


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}