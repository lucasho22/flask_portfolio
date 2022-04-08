{% include navigation.html %}

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@lucasho22/flaskportfolio-2?embed=true"> </iframe>

## Week 4

### Phone Number
```python
@app_crud.route('/authorize/', methods=["GET", "POST"])
def crud_authorize():
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        phone = request.form.get("phone")
        password2 = request.form.get("password1")           # password should be verified
        if authorize(user_name, email, password1, phone):    # zero index [0] used as user_name and email are type tuple
            return redirect(url_for('crud.crud_login'))
    # show the auth user page if the above fails for some reason
    return render_template("authorize.html")
  ```
  ```python
  <td>{{ row['password'] | truncate(20) }}</td>
  ```
  
### Logout and login_required for other part
```python
@app_crud.route('/crud_logout')
  @login_required
  def crud_logout():
    logout_user() # removes login state of user from session
    return render_template("login.html")
```
```python
  <div class="container py-4">
      <span class="fs-4; align-content-end"><a href={{url_for('crud.crud_logout')}}>Logout </a></span>
  </div>
```
