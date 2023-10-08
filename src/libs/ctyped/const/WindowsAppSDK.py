# WindowsAppSDK-VersionInfo
class Release:
    """
    Build-time constants for the Windows App SDK release
    """
    Major = 1
    """
    The major version of the Windows App SDK release.
    """
    Minor = 4
    """
    The minor version of the Windows App SDK release.
    """
    Patch = 0
    """
    The patch version of the Windows App SDK release.
    """
    MajorMinor = 0x00010004
    """
    The major and minor version of the Windows App SDK release, encoded as a uint32_t (0xMMMMNNNN where M=major, N=minor).
    """
    Channel = 'stable'
    """
    The Windows App SDK release's channel; for example, "preview", or empty string for stable.
    """
    VersionTag = ''
    """
    The Windows App SDK release's version tag; for example, "preview2", or empty string for stable.
    """
    VersionShortTag = ''
    """
    The Windows App SDK release's short-form version tag; for example, "p2", or empty string for stable.
    """
    FormattedVersionTag = ''
    """
    The Windows App SDK release's version tag, formatted for concatenation when constructing identifiers; for example, "-preview2", or empty string for stable.
    """
    FormattedVersionShortTag = ''
    """
    The Windows App SDK release's short-form version tag, formatted for concatenation when constructing identifiers; for example, "-p2", or empty string for stable.
    """


class Runtime:
    """
    Build-time constants for the Windows App SDK runtime
    """
    class Identity:
        Publisher = 'CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US'
        """
        The Windows App SDK runtime's package identity's Publisher.
        """
        PublisherId = '8wekyb3d8bbwe'
        """
        The Windows App SDK runtime's package identity's PublisherId.
        """

    class Version:
        Major = 4000
        """
        The major version of the Windows App SDK runtime; for example, 1000.
        """
        Minor = 986
        """
        The minor version of the Windows App SDK runtime; for example, 446.
        """
        Build = 611
        """
        The build version of the Windows App SDK runtime; for example, 804.
        """
        Revision = 0
        """
        The revision version of the Windows App SDK runtime; for example, 0.
        """
        UInt64 = 0x0FA003DA02630000
        """
        The version of the Windows App SDK runtime, as a uint64l for example, 0x03E801BE03240000.
        """
        DotQuadString = '4000.986.611.0'
        """
        The version of the Windows App SDK runtime, as a string (const wchar_t*); for example, "1000.446.804.0".
        """

    class Packages:
        class Framework:
            PackageFamilyName = 'Microsoft.WindowsAppRuntime.1.4_8wekyb3d8bbwe'
            """
            The Windows App SDK runtime's Framework package's family name.
            """

        class Main:
            PackageFamilyName = 'Microsoft.WindowsAppRuntime.1.4_8wekyb3d8bbwe'
            """
            The Windows App SDK runtime's Main package's family name.
            """

        class Singleton:
            PackageFamilyName = 'Microsoft.WindowsAppRuntime.1.4_8wekyb3d8bbwe'
            """
            The Windows App SDK runtime's Singleton package's family name.
            """

        class DDLM:
            class X86:
                PackageFamilyName = 'Microsoft.WindowsAppRuntime.1.4_8wekyb3d8bbwe'
                """
                The Windows App SDK runtime's Dynamic Dependency Lifetime Manager (DDLM) package's family name, for x86.
                """

            class X64:
                PackageFamilyName = 'Microsoft.WindowsAppRuntime.1.4_8wekyb3d8bbwe'
                """
                The Windows App SDK runtime's Dynamic Dependency Lifetime Manager (DDLM) package's family name, for x64.
                """

            class Arm64:
                PackageFamilyName = 'Microsoft.WindowsAppRuntime.1.4_8wekyb3d8bbwe'
                """
                The Windows App SDK runtime's Dynamic Dependency Lifetime Manager (DDLM) package's family name, for arm64.
                """
