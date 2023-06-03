let form = document.getElementById('form');
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
    setuserdetails();
});
var csrftoken = getCookie('csrftoken'); // Implement the 'getCookie' function to retrieve the CSRF token from the cookie

var headers = new Headers();
headers.append('Content-Type', 'multipart/form-data');
headers.append('X-CSRFToken', csrftoken);

const setuserdetails = async () => {
    // var name = document.getElementById('empname').value;
    // var email = document.getElementById('empemail').value;
    // var department = document.getElementById('empdepartment').value;
    // var description = document.getElementById('empdesc').value;
    // var fileInput = document.getElementById('fileupload');
    var form = document.getElementById('form');
    var formData = new FormData(form);
    // formData.append('empname', name);
    // formData.append('empemail', email);
    // formData.append('empdepartment', department);
    // formData.append('empdescription', description);
    // formData.append('fileupload', fileInput.files[0]);
    try {
        const url = 'http://127.0.0.1:8000/getdetails/';
        console.log('error')
        let response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: formData,
            // body: JSON.stringify(data), // you can just skip this if all you want is to test the API
        })
        res = await response.json()
        console.log('response', res);
    } catch (error) {
        console.log('error is: ', error)
    }

}  