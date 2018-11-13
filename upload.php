<?php 

if(isset($_FILES['file'])) { 
	$file = $_FILES['file'];

	$file_name = $file['name'];
	$file_tmp = $file['tmp_name'];
	$file_size = $file['size'];
	$file_error = $file['error'];

	//ensure only jpg/ png allowed
	$file_ext = explode('.', $file_name);
	$file_ext = strtolower(end($file_ext));

	$allowed = array('png', 'jpg');

	if(in_array($file_ext, $allowed)){
		if($file_error == 0) {
			if($file_size <= 2097555) {
				//create unique id for each file uploaded, if same name is inputted,
				//then previous file will be overwritten
				$file_name_new = uniqid('', true) . '.' . $file_ext;
				//specify destination
				$file_destination = 'uploads/' . $file_name_new;

				move_uploaded_file($file["$file_tmp"], "training-data/" . $file["$file_name_new"]);

			}
			}
		}

	}

}


//header("Location: application.py");

?>