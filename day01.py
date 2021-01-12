from conans import ConanFile, CMake, tools

class DevopsConan(ConanFile):
    name = "Day01"
    version = "0.1.0"
    license = "<Put the package license here>"
    author = "FDTech GmbH"
    url = "https://github.com/1ikH52qOr8lkHCpcFymf/devops_ccsd_tech_challenge_conan_day01.git"
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
        if (tools.get_env("BUILD_UNIT_TESTS") == "ON"):
            self.build_requires("gtest/1.8.1@")
        self.build_requires("Utils/0.1.0@devops/testing")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = "OFF"
        if (tools.get_env("BUILD_UNIT_TESTS") == "ON"):
            cmake.definitions["BUILD_UNIT_TESTS"] = "ON"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        if (tools.get_env("BUILD_UNIT_TESTS") == "ON"):
            cmake.test()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def deploy(self):
        self.copy("*")

    def package_id(self):
        del self.info.settings.compiler
