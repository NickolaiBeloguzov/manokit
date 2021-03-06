# Copyright (C) 2021  Nickolai Beloguzov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# manokit.exceptions module
#
# Provides custom exceptions for manokit package


class NotAValidEmailAddressError(Exception):
    def __init__(self, *args: object) -> None:
        """
        Email address is not valid
        """
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class AttachmentError(Exception):
    def __init__(self, *args: object) -> None:
        """
        An email's attachment is not valid
        """
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class BodyError(Exception):
    def __init__(self, *args: object) -> None:
        """
        An email's body is not valid
        """
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class ParameterError(Exception):
    def __init__(self, *args: object) -> None:
        """
        One or more function's parameters is invalid
        """
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class AuthError(Exception):
    def __init__(self, *args: object) -> None:
        """
        There's an error during authentication
        """
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class SMTPError(Exception):
    def __init__(self, *args: object) -> None:
        """
        There's an error with SMTP Server
        """

        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()


class EmailError(Exception):
    def __init__(self, *args: object) -> None:
        """
        Email cannot be sent
        """
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()
