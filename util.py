# FILESYSTEM

	#get folder path of script
		os.path.dirname(os.path.abspath(__file__))

	#failsafely create directory
		if not os.path.exists("/tmp/xml_dump"):
			os.makedirs("/tmp/xml_dump")

	#move a file
	os.rename(SOURCE, DESTINATION)

	#get all files in a folder
		all_script_templates = os.walk(setup_scripts_folder).__next__()[2]

	#get all folders in a folder
		all_script_templates = os.walk(setup_scripts_folder).__next__()[1]
	# For the last to: Usually you want to recursively go through all subdirectories.
	# For this it's better to just loop with an normal os.walk on the root folder.

def find_filename(prefix, fileending=".txt", counter=2, formatstring="{}_{}"):
	"""Return a non-existing filename."""

	if os.path.exists(prefix+fileending):
		if type(counter) == str:
			if any(x in counter for x in ["%S", "%c", "%X"]):
				uniqueID = time.strftime(counter) #   "%Y%m%dT%H%M%S"
			else:
				raise ValueError("Format string does not contain seconds. Runtime could be longer than a minute.")
		elif type(counter) in (int, float):
			uniqueID = int(counter)
		else:
			raise TypeError("Argument 'counter' must be a time format string or a number.")

		while os.path.exists(formatstring+"{}".format(prefix,uniqueID,fileending)):
			if type(counter) == str:
				time.sleep(1)
				uniqueID = time.strftime(counter)
			elif type(counter) in (int, float):
				uniqueID += 1
		unique_filename = formatstring.format(prefix,uniqueID)
	return unique_filename + fileending

# CALLING SERVICES
	#update svn repo
		os.chdir(SVN_PATH)
		with open(os.devnull, 'w') as devnull:
			subprocess.call(["svn","update"], stdout=devnull)

	#call an XML RPC method
		args.address = "IPADDRESS of RPC server"
		controller = xmlrpc.client.ServerProxy('http://' + args.address + ':2001')
		result = controller.getDeviceDescription(ARGUMENT1, ARGUMENT2)
		result = controller.getValue("DEVICE:CHANNEL", "POINTID")

	#set status in systemctl
		subprocess.call(["systemd-notify","--status=STATUSMESSAGEHERE"])

	#log to systemctl journal (journalctl)
		print("LOGMESSAGEHERE",flush=True)
		#You will also need to specify the "NotifyAccess=main" option in the service file.

# FILETYPES AND FILE OPERATIONS
	#dynamically load module MODULENAME
		webform_parser = __import__("MODULENAME")

	#open config file
		config = configparser.ConfigParser(default_section="GENERAL", empty_lines_in_values=False)
		config.read(FILENAMEHERE)

	#update config file
		with open(CONFIGFILENAME, 'w', encoding="utf-8") as config_file:
			config.write(config_file)

	#initializing a config file
	if not config.has_section("GENERAL"):
		config["GENERAL"] = {
			"last_inbox_check": "0.0",
			"last_status_mail": "0.0"
		}

	#open json file
		with open(args.data, encoding="utf-8") as data_file:
			location_data = json.load(data_file)

	#open excel sheet
		wb = load_workbook(filename=FILENAMEHERE, read_only=True)
		data_sheet = wb[wb.get_sheet_names()[0]]

	#open XML file:
		current_xml = ET.fromstring(device_description_file.read())
		current_xml = ET.fromstring(xml_results)
		desc_type = current_xml.find("BASEDESCRIPTION").find("BASE").attrib["TYPE"]
		desc_version = current_xml.find("BASEDESCRIPTION").find("BASE").attrib["VER"]

	#open mako template
		this_template = mako_Template(filename=FILENAMEHERE,
								module_directory="template_cache",
								input_encoding='utf-8',
								output_encoding='utf-8',
								default_filters=['decode.utf8'])

	#render mako template
		with open(WRITEFILENAME, "w", encoding="utf-8") as this_setup_script:
			this_setup_script.write(
				this_template.render_unicode(
					data=VARIABLE,
					filename=OTHERVARIABLE
				)
			)

	#writing to a json file
		with open(FILENAMEHERE, "w", encoding="utf-8") as data_file:
			json.dump(DICTIONARYHERE, data_file, indent=4, separators=(',', ': '), sort_keys=True, ensure_ascii=False)

	#write list to file as lines in one command
		FILEOBJECTHERE.write('\n'.join(LISTVARHERE))
	# or:
		print(*LISTVARHERE, sep='\n', file=FILEOBJECTHERE)

	#writing to a csv file
		with open(FILENAMEHERE, "w", encoding="utf-8") as dofile:
			dofile_writer = csv.DictWriter(dofile, fieldnames=["First Name","Second Name"], lineterminator="\n")
			if device_list_file.mode in ["w", "b"]:
				dofile_writer.writeheader()
			for row in rows:
				dofile_writer.writerow({"First Name":row[0],"Second Name":row[1]})

# DATA PROCESSING
	#import modules dynamically
		technology_names = os.walk(os.path.join(os.getcwd(),"technologies")).__next__()[1]
		technologies = {}
		for technology in technology_names:
			if technology != "__pycache__":
				technologies[technology] = importlib.import_module("technologies."+technology+".adapter")

	#go through dictionary
		for device_id in sorted(device_types.keys()):

	#get lines and strip newlines in one command
		with open(args.fileB) as file_B:
			lines = file_B.read().splitlines()

	#go through excel column
		for cell_index in range(1,150):
			current_cell_value = str(data_sheet["F"+str(cell_index)].value)

	#check if at least one item of a list is contained in the other list
		if any(i in biglist for i in smalllist):
	# or if the items in the list should not repeat anyways:
		if len(set(listA) & set(listB)) > 0:

	#get matched group of regex match
		re_match.group("groupname")

	#convert bytestring to normal string
		str(STRINGVAR,"utf-8")

# OUTPUT

#print something with no indentation
	print("FIRST LINE HERE\n"
			"SECOND LINE HERE\n"
			"THIRD LINE HERE".format(config_file=complete_output_filename))

#print something over several lines
	print("FIRST LINE HERE"
			"SECOND LINE HERE"
			"THIRD LINE HERE".format(config_file=complete_output_filename),
			sep="\n")

#pad a number with 0s:
	"SOMESTRING{:0>8}".format(SOMENUMBER)

#truncate digits after the mark/comma:
	"{bla:.5f}".format(bla=0.8999923704890517)
	(returns 0.899992)
