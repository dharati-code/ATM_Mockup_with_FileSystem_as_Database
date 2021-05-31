# create record
# update record
# read record
# delete record
# CRUD

# find user

import os
import validation
import re
import shutil

user_db_path = "data/user_record/"
auth_folder = "auth_session/session/"


def createdir(input_dir):
    """Given a directory, this function either creates a directory from the current working directory
        or prints saying that the directory exists

    Args:
        input_dir ([string]): provide a string with the path e.g. user_db_path variable, etc
    """
    # check if dir exists
    current_dir = os.path.dirname(__file__)
    full_path = os.path.join(current_dir, input_dir)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"{input_dir} dir created")


def create(user_account_number, first_name, last_name, email, password):
    """

    Args:
        user_account_number ([string]): user account number
        first_name ([string]): first name
        last_name ([string]): last name
        email ([string]): email
        password ([string]): password

    Returns:
        [Boolean]: True or False
    """
    # create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # return true
    # if saving to file fails, then deleted created file

    user_data = (
        first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    )

    if does_account_number_exist(user_account_number):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(user_account_number) + ".txt", "x")
        f.write(str(user_data))
        completion_state = True

    except FileExistsError:

        filesize = os.path.getsize(user_db_path + str(user_account_number) + ".txt")
        if filesize == 0:
            delete(user_account_number)
    finally:

        f.close()
        return completion_state


def read(user_account_number):

    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def update(user_account_number, balance):
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true

    with open(user_db_path + str(user_account_number) + ".txt", "r+") as f:
        text = f.read()
        text = re.sub(text.split(',')[4], balance, text)
        f.seek(0)
        f.write(text)
        f.truncate()
        return True

def delete(user_account_number):

    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):

        try:

            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful

def auth_delete(user_account_number):

    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False

    if os.path.exists(auth_folder + str(user_account_number) + ".txt"):

        try:

            os.remove(auth_folder + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful

def auth_create(user_account_number):
    # fetch the user data from user_db_path
    createdir(auth_folder)
    is_auth_successful = False
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            shutil.copy(os.path.join(user_db_path, str(user_account_number) + ".txt"), auth_folder)
            is_auth_successful = True
        except FileNotFoundError:
            print("User not found during auth_create")
        finally:
            return is_auth_successful




def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ",")
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):

    createdir(user_db_path)
    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number) + ".txt":

            return True

    return False


def authenticated_user(account_number, password):

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ",")
        if password == user[3]:
            return user

    return False