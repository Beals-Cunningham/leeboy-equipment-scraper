import express from 'express'

const app = express()

app.get('/', (req, res) => {
    res.type('html')
    res.setHeader('Surrogate-Control', 'no-store'); res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate'); res.setHeader('Pragma', 'no-cache'); res.setHeader('Expires', '0')
    res.sendFile('/web/views/index.html', { root: '.' })
})

app.get('/jquery/js', (req, res) => {
    res.type('js')
    res.sendFile('/node_modules/jquery/dist/jquery.min.js', { root: '.' })
})

app.get('/jq.js', (req, res) => {
    res.type('js')
    res.sendFile('/web/js/jq.js', { root: '.' })
})

app.get('/get.js', (req, res) => {
    res.type('js')
    res.sendFile('/web/js/get.js', { root: '.' })
})

app.get('/process.js', (req, res) => {
    res.type('js')
    res.sendFile('/web/js/process.js', { root: '.' })
})

app.get('/direct.js', (req, res) => {
    res.type('js')
    res.sendFile('/web/js/direct.js', { root: '.' })
})

app.get('/pages.js', (req, res) => {
    res.type('js')
    res.sendFile('/web/js/pages.js', { root: '.' })
})

app.get('/soup.riv', (req, res) => {
    res.sendFile('/web/assets/soup.riv', { root: '.', headers: { 'Content-Type': 'riv' } })
})

app.get('/go.riv', (req, res) => {
    res.sendFile('/web/assets/go.riv', { root: '.', headers: { 'Content-Type': 'riv' } })
})

app.listen(7060, () => {
    console.log('Listening on port 7060')
})