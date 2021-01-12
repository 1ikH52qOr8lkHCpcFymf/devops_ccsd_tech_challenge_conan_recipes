from conans import ConanFile, CMake, tools


class DevopsConan(ConanFile):
    name = "Utils"
    version = "0.1.0"
    license = "<Put the package license here>"
    author = "FDTech GmbH"
    url = "https://github.com/1ikH52qOr8lkHCpcFymf/devops_ccsd_tech_challenge_conan_utils.git"
    description = "{}".format(name)
    settings = "os", "compiler", "build_type", "arch"
    options = None
    default_options = None
    generators = "cmake"

    scm = {
        "type":     "git",
        "revision": "master",
        "url":      url
    }

    def build_requirements(self):
        self.build_requires("cmake/3.19.2@")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def deploy(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = ["utilslib"]
