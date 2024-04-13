
// sending request to the backend without AJAX 

function deleteNote(note_id){
    // endpoint - here we sending our function
   
    url = '/delete-note'
    note = {
        note_id:note_id
    }
    // sending post - note.id to the server
    // sever getting responde throught get
    const request = new Request(url,{

        method:'POST',
        headers:new Headers({
            'Content-Type':'application/json;charset=utf-8'
        }),
        body:JSON.stringify(note)
        
    })

    fetch(request)
    .then(res => {return res.json()}) // res => console.log(res)
    .then(res => console.log(res))
    .then(res => window.location.href = "/") // home page refresh
         
}

// done task check box


