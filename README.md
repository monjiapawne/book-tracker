## About `book_tracker`
- `book_tracker` is a `YAML` configured book tracker, that renders to markdown, targeted for `gfm`.  
- It is meant to be very high level, while still providing a solid level of customization.  
  
## How to setup  
- Fork this repo  
- Configure `book_process.yaml`  
- (Optional) Configure `config.yaml`  
  
### `book_process.yaml` fields  
```yaml  
book_data:  
  - heading: heading name  
    heading_depth: 4  
      
  cover_art:  
    scale: scale of cover art, or set in config globally  
  comment_before: comment before books  
  comment_after: comment after books  
  
  books:  
  - title: book title  
    auther: author  
    page: current page  
    total_pages: total pages  
    cover_art: name_of_cover_art.png  
```  
  
### `config.yaml` fields  
```yaml  
config:  
  progress_bar:  
    length: length of bar  
    fill_char: fill emoji  
    empty_char: unfilled emoji  
  global_cover_art:  
    scale: scale multiplier  
    width: width in px  
    height: height in px  
```

## Reading

| Title |Author |Progress |Page |
|--|--|--|--|
|Effective Python |Brett Slatkin |███████░░░░░░░░░░░░░░░░░░░░░░░░ 23% |112/472 |
|Site Reliability Engineering |Google |████░░░░░░░░░░░░░░░░░░░░░░░░░░░ 14% |82/550 |
|Kubernetes 101 |Jeff Geerling |█████████████░░░░░░░░░░░░░░░░░░ 42% |55/128 |
|The Code Book |Simon Singh |██████████░░░░░░░░░░░░░░░░░░░░░ 34% |93/273 |
<p align='left'><img src='cover_art/cover_art_post/effective_python.png' alt='Effective Python_cover' width='75' height='112'><img src='cover_art/cover_art_post/site_reliability_engineering.png' alt='Site Reliability Engineering_cover' width='75' height='112'><img src='cover_art/cover_art_post/kubernetes_101.png' alt='Kubernetes 101_cover' width='75' height='112'><img src='cover_art/cover_art_post/the_code_book.png' alt='The Code Book_cover' width='75' height='112'></p>


## Read
Book I've read.
<p align='left'><img src='cover_art/cover_art_post/devops_handbook.png' alt='DevOps HandBook_cover' width='150' height='225'></p>


## Future
Future books I'll read.
<p align='left'><img src='cover_art/cover_art_post/fluent_python.png' alt='Fluent Python_cover' width='150' height='225'><img src='cover_art/cover_art_post/nginx_cookbook.png' alt='Nginx Cookbook_cover' width='150' height='225'></p>


#### Investigate Further

<p align='left'><img src='cover_art/cover_art_post/fluent_python.png' alt='Fluent Python_cover' width='120' height='180'><img src='cover_art/cover_art_post/nginx_cookbook.png' alt='Nginx Cookbook_cover' width='120' height='180'></p>


